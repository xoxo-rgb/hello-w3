class NuitkaErrorBase(Exception):
    pass


class NuitkaNodeError(NuitkaErrorBase):

    # Try to output more information about nodes passed.
    def __str__(self):
        try:
            from nuitka.codegen.Indentation import indented

            parts = [""]

            for arg in self.args:  # false alarm, pylint: disable=I0021,not-an-iterable
                if hasattr(arg, "asXmlText"):
                    parts.append(indented("\n%s\n" % arg.asXmlText()))
                else:
                    parts.append(str(arg))

            parts.append("")
            parts.append("The above information should be included in a bug report.")

            return "\n".join(parts)
        except Exception as e:  # Catch all the things, pylint: disable=broad-except
            return "<NuitkaNodeError failed with %r>" % e


class NuitkaOptimizationError(NuitkaNodeError):
    pass


class NuitkaAssumptionError(AssertionError):
    pass
