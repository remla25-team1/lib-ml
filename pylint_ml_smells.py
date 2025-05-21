# File: pylint_ml_smells.py
import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class MLCodeSmellChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'ml-code-smell-checker'
    priority = -1
    msgs = {
        'C9001': (
            'Model training and prediction are tightly coupled (fit() followed by predict() in the same function)',
            'ml-training-predict-coupling',
            'Avoid calling fit() and predict() in the same function. Separate training and inference logic.'
        ),
    }

    def visit_functiondef(self, node):
        """Detects fit() followed by predict() within a single function body"""
        saw_fit = False
        for call in node.nodes_of_class(astroid.nodes.Call):
            func_expr = call.func.as_string()
            if func_expr.endswith('.fit'):
                saw_fit = True
            if saw_fit and func_expr.endswith('.predict'):
                self.add_message('C9001', node=node)
                break

def register(linter):
    linter.register_checker(MLCodeSmellChecker(linter))
