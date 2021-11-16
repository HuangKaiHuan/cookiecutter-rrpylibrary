from gitlint.contrib.rules.conventional_commit import ConventionalCommit


class ConventionalCommit2(ConventionalCommit):
    """
    Force ignore Merge commits
    """

    id = "CT2"

    def validate(self, line, _commit):
        if line.startswith("Merge"):
            return []
        else:
            return super(ConventionalCommit2, self).validate(line, _commit)
