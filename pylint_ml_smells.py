import astroid
from pylint.checkers import BaseChecker
from pylint.lint import PyLinter

class MLCodeSmellChecker(BaseChecker):
    """
    Detect cases where fit() is immediately followed by predict()
    within the same function, indicating training/inference coupling.
    """
    name = 'ml-code-smell-checker'
    priority = -1
    msgs = {
        'C9001': (
            'Model training and prediction are tightly coupled '
            '(fit() followed by predict() in the same function)',
            'ml-training-predict-coupling',
            'Avoid calling fit() and predict() in the same function. '
            'Separate training and inference logic.'
        ),
    }

    def visit_functiondef(self, node: astroid.nodes.FunctionDef):
        """Walk all Call nodes in the function and flag fit→predict sequences."""
        saw_fit = False
        # Iterate over all call expressions in this function
        for call in node.nodes_of_class(astroid.nodes.Call):
            func_expr = call.func.as_string()
            if func_expr.endswith('.fit'):
                saw_fit = True
            elif saw_fit and func_expr.endswith('.predict'):
                # Once a predict follows a fit, emit the message
                self.add_message('C9001', node=node)
                break

def register(linter: PyLinter):
    """Register the checker to Pylint."""
    linter.register_checker(MLCodeSmellChecker(linter))
