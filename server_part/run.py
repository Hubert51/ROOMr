#!/Users/gengruijie/envs/lsbaws/bin/python

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from app import app
app.run(debug=True)