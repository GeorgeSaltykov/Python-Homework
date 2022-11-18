import module_import as mod_i
import module_export as mod_ex
import view


def start():
    x = view.user_choice()
    if x == 'w':
        mod_ex.writing(view.answer())
    else:
        mod_i.showing(x)
