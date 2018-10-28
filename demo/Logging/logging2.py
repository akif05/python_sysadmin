import logging
from systemd.journal import JournalHandler

# Logging to a file
logging.basicConfig(filename="example.log", level=logging.WARN,
                    format="%(levelname)s %(asctime)s %(message)s")
logging.warning("This is a formatted warning")

# Logging to the systemd journal
jlogger = logging.getLogger("journal-logger")
jhandler = JournalHandler()
jformatter = logging.Formatter(fmt="%(levelname)s %(message)s")
jhandler.setFormatter(jformatter)

jlogger.addHandler(jhandler)
jlogger.warning("This is a warning sent to the journal")

# Prevent the message propagating to the root logger, but only to journal
jlogger.propagate = False
jlogger.warning("Warning ONLY to journal")

def bad_idea():
    try:
        c = 1 / 0
    except:
        logging.error("Failed to devide", exc_info=True)

bad_idea()