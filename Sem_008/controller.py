import module_import as mod_i
import module_export as mod_ex
import view
import logger


def start():
    view.file_contains()
    x = view.user_choice()
    while x != 'q':
        if x == 'w':
            mod_ex.writing(view.answer())
            logger.log(True)
        elif x == 'all':
            mod_i.show_everything()
            logger.log(False)
        else:
            mod_i.showing(x)
            logger.log(False)
        view.file_contains()
        x = view.user_choice()
