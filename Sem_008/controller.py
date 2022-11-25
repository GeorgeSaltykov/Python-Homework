import module_import as mod_i
import module_export as mod_ex
import view


def start():
    view.file_contains()
    x = view.user_choice()
    while x != 'q':
        if x == 'w':
            mod_ex.writing(view.answer())
        elif x == 'all':
            mod_i.show_everything()
        else:
            mod_i.showing(x)
        view.file_contains()
        x = view.user_choice()
