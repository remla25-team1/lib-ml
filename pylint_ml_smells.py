from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class MLCodeSmellChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'ml-code-smell-checker'
    priority = -1
    msgs = {
        'C9001': (
            'Model training and prediction are tightly coupled (fit() followed by predict() in same function)',
            'ml-training-predict-coupling',
            'Avoid calling fit() and predict() in the same function; separate training and inference.'
        ),
    }

    def visit_functiondef(self, node):
        fit_found = False
        predict_found = False
        for child in node.body:
            if hasattr(child, 'as_string'):
                line = child.as_string()
                if '.fit(' in line:
                    fit_found = True
                if '.predict(' in line and fit_found:
                    predict_found = True
        if fit_found and predict_found:
            self.add_message('C9001', node=node)

def register(linter):
    linter.register_checker(MLCodeSmellChecker(linter))
