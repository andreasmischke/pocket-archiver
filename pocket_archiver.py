import config
import retrieve

if __name__ == "__main__":

    if not config.enable_rollbar:
        print(retrieve.get_whole_archive())

    else:
        import rollbar
        rollbar.init(config.rollbar_key, config.rollbar_level)

        try:
            print(retrieve.get_whole_archive())
        except:
            rollbar.report_exc_info()

        rollbar.report_message("executed pocket_archiver", "info")

