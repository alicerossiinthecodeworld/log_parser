import json
import sys
from datetime import datetime

import formatter

#### Настройки_файла или директории
FILEPATH = "/Users/anproskuryakova/PycharmProjects/log_parser/dir/access.log"
DIRPATH = "/Users/anproskuryakova/PycharmProjects/log_parser/dir"

PATH = FILEPATH

report = formatter.format_the_report_dict(PATH)
with open(f"result_{datetime.now().strftime('%d-%m-%Y-%H:%M-scan')}.json", "w") as outfile:
    json.dump(report, outfile)
sys.stdout.write(str(report))
