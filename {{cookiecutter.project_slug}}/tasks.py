from invoke import task

import versioneer


@task
def clean(c, docs=False, bytecode=False, extra=""):
    patterns = ["build", "src/*.egg-info/"]
    if docs:
        patterns.append("docs/_build")
    if bytecode:
        patterns.append("**/*.pyc")
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))


@task
def build(c, docs=False):
    c.run("python setup.py build")
    if docs:
        c.run("tox -e docs")


@task(help={"part": "part of the version to be bumped"})
def bumpversion(c, part):
    if part not in ("major", "minor", "patch"):
        raise ValueError('part must be one of "major", "minor", or "patch"!')

    git_status_result = c.run("git status --porcelain")
    if len(git_status_result.stdout):
        raise RuntimeError(
            f"Git working directory is not clean:\n{git_status_result.stdout}"
        )

    c.run("gitchangelog")
    git_status_result = c.run("git status --porcelain")
    if len(git_status_result.stdout) == 0:
        raise RuntimeError(
            "Empty Change! you must have at least one commit type of fix, feat or breaking change"
        )

    full_version = versioneer.get_versions()["version"]
    major, minor, patch = [int(i) for i in full_version.split("+")[0].split(".")]
    if part == "patch":
        patch += 1
    elif part == "minor":
        minor += 1
        patch = 0
    else:
        major += 1
        minor = 0
        patch = 0
    new_version = f"{major}.{minor}.{patch}"
    c.run(f"git tag {new_version}")
    c.run("gitchangelog")
    c.run("git add CHANGELOG.rst")
    c.run(f"git commit -m 'chore: bump version -> {new_version}'")
    c.run(f"git tag -f {new_version}")


@task
def lint_commit(c):
    git_rev_list_result = c.run("git rev-list --max-parents=0 HEAD")
    first_commit_sha = git_rev_list_result.stdout.splitlines()[0]
    c.run(f"gitlint --commits '{first_commit_sha}..HEAD'")
