# ENCRYPTED by : Golu Molu
# Created by : Golu Molu
# Github : https://github.com/fkunknownteam

import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
