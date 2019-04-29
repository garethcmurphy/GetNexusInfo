#!/usr/bin/env python3
import h5py
import inspect
import copy
import json
import socket


class GetNexusInfo:
    nexusInfo = {}
    filename = "v20.h5"
    metadata = {}
    sfdict = {}
    basename = "/users/detector/experiments/"

    sourceFolderArray = {
        "0001": "v20/2018_01_24",
        "0002": "v20/2018_12_13/v20-2018-12-14T11:22:26+0100",
        "0003": "v20/2018_12_13/v20-2018-12-14T11:23:38+0100",
        "0004": "v20/2018_12_13/v20-2018-12-14T15:12:53+0100",
        "0005": "v20/2018_12_13/v20-2018-12-14T16:12:01+0100",
        "0006": "v20/2018_12_13/v20-2018-12-14T16:12:26+0100",
        "0007": "v20/2018_12_13/v20-2018-12-15T16:56:22+0100",
        "0008": "v20/2018_12_13/v20-2018-12-15T18:10:22+0100",
        "0009": "v20/2018_12_13/v20-2018-12-17T07:13:37+0100",
        "0010": "v20/2018_12_13/v20-2018-12-17T19:31:02+0100",
        "0011": "v20/2018_12_13/v20-2018-12-18T09:18:46+0100",
        "0012": "v20/2018_12_13/v20-2018-12-18T10:42:33+0100",
        "0013": "v20/2018_12_13/v20-2018-12-18T11:01:28+0100",
        "0014": "v20/2018_12_13/v20-2018-12-19T08:17:32+0100",
        "0015": "v20/2018_12_13/v20-2018-12-19T08:56:00+0100",
        "0016": "v20/2018_12_13/V20_ESSIntegration_20181210",
        "0017": "v20/2018_12_13/V20_ESSIntegration_2018-12-10_1009",
        "0018": "v20/2018_12_13/V20_ESSIntegration_2018-12-10_1805",
        "0019": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0915",
        "0020": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0943",
        "0021": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0951",
        "0022": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0952",
        "0023": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1018",
        "0024": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1713",
        "0025": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1743",
        "0026": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1847",
        "0027": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1914",
        "0028": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1923",
        "0029": "v20/2018_12_13/V20_ESSIntegration_2018-12-12_1209",
        "0030": "v20/2018_12_13/V20_ESSIntegration_2018-12-13_0942",
        "0031": "v20/2018_12_13/V20_ESSIntegration_2018-12-13_1028",
        "0032": "v20/2018_12_13/V20_ESSIntegration_2018-12-13T15:53:48",
        "0033": "v20/2018_12_13/V20_ESSIntegration_2018-12-13T16:20:00",
        "0034": "v20/2018_12_13/V20_ESSIntegration_2018-12-14T09:25:00",
        "0036": "v20/2019_04_05/nicos_00000022.hdf",
        "0037": "v20/2019_04_05/nicos_00000023.hdf",
        "0038": "v20/2019_04_05/nicos_00000024.hdf",
        "0039": "v20/2019_04_05/nicos_00000025.hdf",
        "0040": "v20/2019_04_05/nicos_00000026.hdf",
        "0041": "v20/2019_04_05/nicos_00000027.hdf",
        "0042": "v20/2019_04_05/nicos_00000028.hdf",
        "0043": "v20/2019_04_05/nicos_00000029.hdf",
        "0044": "v20/2019_04_05/nicos_00000030.hdf",
        "0045": "v20/2019_04_05/nicos_00000031.hdf",
        "0046": "v20/2019_04_05/nicos_00000032.hdf",
        "0047": "v20/2019_04_05/nicos_00000033.hdf",
        "0048": "v20/2019_04_05/nicos_00000034.hdf",
        "0049": "v20/2019_04_05/nicos_00000035.hdf",
        "0050": "v20/2019_04_05/nicos_00000036.hdf",
        "0051": "v20/2019_04_05/nicos_00000037.hdf",
        "0052": "v20/2019_04_05/nicos_00000038.hdf",
        "0053": "v20/2019_04_05/nicos_00000039.hdf",
        "0054": "v20/2019_04_05/nicos_00000040.hdf",
        "0055": "v20/2019_04_05/nicos_00000041.hdf",
        "0056": "v20/2019_04_05/nicos_00000042.hdf",
        "0057": "v20/2019_04_05/nicos_00000043.hdf",
        "0058": "v20/2019_04_05/nicos_00000044.hdf",
        "0059": "v20/2019_04_05/nicos_00000045.hdf",
        "0060": "v20/2019_04_05/nicos_00000047.hdf",
        "0061": "v20/2019_04_05/nicos_00000048.hdf",
        "0062": "v20/2019_04_05/nicos_00000049.hdf",
        "0063": "v20/2019_04_05/nicos_00000050.hdf",
        "0064": "v20/2019_04_05/nicos_00000051.hdf",
        "0065": "v20/2019_04_05/nicos_00000052.hdf",
        "0066": "v20/2019_04_05/nicos_00000053.hdf",
        "0067": "v20/2019_04_05/nicos_00000054.hdf",
        "0068": "v20/2019_04_05/nicos_00000055.hdf",
        "0069": "v20/2019_04_05/nicos_00000056.hdf",
        "0070": "v20/2019_04_05/nicos_00000058.hdf",
        "0071": "v20/2019_04_05/nicos_00000059.hdf",
        "0072": "v20/2019_04_05/nicos_00000060.hdf",
        "0073": "v20/2019_04_05/nicos_00000061.hdf",
        "0074": "v20/2019_04_05/nicos_00000062.hdf",
        "0075": "v20/2019_04_05/nicos_00000063.hdf",
        "0076": "v20/2019_04_05/nicos_00000064.hdf",
        "0077": "v20/2019_04_05/nicos_00000065.hdf",
        "0078": "v20/2019_04_05/nicos_00000066.hdf",
        "0079": "v20/2019_04_05/nicos_00000067.hdf",
        "0080": "v20/2019_04_05/nicos_00000068.hdf",
        "0081": "v20/2019_04_05/nicos_00000069.hdf",
        "0082": "v20/2019_04_05/nicos_00000070.hdf",
        "0083": "v20/2019_04_05/nicos_00000071.hdf",
        "0084": "v20/2019_04_05/nicos_00000072.hdf",
        "0085": "v20/2019_04_05/nicos_00000073.hdf",
        "0086": "v20/2019_04_05/nicos_00000074.hdf",
        "0087": "v20/2019_04_05/nicos_00000075.hdf",
        "0088": "v20/2019_04_05/nicos_00000076.hdf",
        "0089": "v20/2019_04_05/nicos_00000077.hdf",
        "0090": "v20/2019_04_05/nicos_00000078.hdf",
        "0091": "v20/2019_04_05/nicos_00000079.hdf",
        "0092": "v20/2019_04_05/nicos_00000080.hdf",
        "0093": "v20/2019_04_05/nicos_00000081.hdf",
        "0094": "v20/2019_04_05/nicos_00000082.hdf",
        "0095": "v20/2019_04_05/nicos_00000083.hdf",
        "0096": "v20/2019_04_05/nicos_00000084.hdf",
        "0097": "v20/2019_04_05/nicos_00000085.hdf",
        "0098": "v20/2019_04_05/nicos_00000086.hdf",
        "0099": "v20/2019_04_05/nicos_00000087.hdf",
        "0100": "v20/2019_04_05/nicos_00000088.hdf",
        "0101": "v20/2019_04_05/nicos_00000090.hdf",
        "0102": "v20/2019_04_05/nicos_00000091.hdf",
        "0103": "v20/2019_04_05/nicos_00000092.hdf",
        "0104": "v20/2019_04_05/nicos_00000093.hdf",
        "0105": "v20/2019_04_05/nicos_00000094.hdf",
        "0106": "v20/2019_04_05/nicos_00000095.hdf",
        "0107": "v20/2019_04_05/nicos_00000096.hdf",
        "0108": "v20/2019_04_05/nicos_00000097.hdf",
        "0109": "v20/2019_04_05/nicos_00000098.hdf",
        "0110": "v20/2019_04_05/nicos_00000099.hdf",
        "0111": "v20/2019_04_05/nicos_00000100.hdf",
        "0112": "v20/2019_04_05/nicos_00000101.hdf",
        "0113": "v20/2019_04_05/nicos_00000102.hdf",
        "0114": "v20/2019_04_05/nicos_00000103.hdf",
        "0115": "v20/2019_04_05/nicos_00000104.hdf",
        "0116": "v20/2019_04_05/nicos_00000105.hdf",
        "0117": "v20/2019_04_05/nicos_00000106.hdf",
        "0118": "v20/2019_04_05/nicos_00000107.hdf",
        "0119": "v20/2019_04_05/nicos_00000108.hdf",
        "0120": "v20/2019_04_05/nicos_00000109.hdf",
        "0121": "v20/2019_04_05/nicos_00000110.hdf",
        "0122": "v20/2019_04_05/nicos_00000111.hdf",
        "0123": "v20/2019_04_05/nicos_00000112.hdf",
        "0124": "v20/2019_04_05/nicos_00000113.hdf",
        "0125": "v20/2019_04_05/nicos_00000114.hdf",
        "0126": "v20/2019_04_05/nicos_00000115.hdf",
        "0127": "v20/2019_04_05/nicos_00000116.hdf",
        "0128": "v20/2019_04_05/nicos_00000117.hdf",
        "0129": "v20/2019_04_05/nicos_00000118.hdf",
        "0130": "v20/2019_04_05/nicos_00000119.hdf",
        "0131": "v20/2019_04_05/nicos_00000120.hdf",
        "0132": "v20/2019_04_05/nicos_00000121.hdf",
        "0133": "v20/2019_04_05/nicos_00000122.hdf",
        "0134": "v20/2019_04_05/nicos_00000123.hdf",
        "0135": "v20/2019_04_05/nicos_00000124.hdf",
        "0136": "v20/2019_04_05/nicos_00000125.hdf",
        "0137": "v20/2019_04_05/nicos_00000126.hdf",
        "0138": "v20/2019_04_05/nicos_00000127.hdf",
        "0139": "v20/2019_04_05/nicos_00000128.hdf",
        "0140": "v20/2019_04_05/nicos_00000129.hdf",
        "0141": "v20/2019_04_05/nicos_00000130.hdf",
        "0142": "v20/2019_04_05/nicos_00000131.hdf",
        "0143": "v20/2019_04_05/nicos_00000132.hdf",
        "0144": "v20/2019_04_05/nicos_00000133.hdf",
        "0145": "v20/2019_04_05/nicos_00000134.hdf",
        "0146": "v20/2019_04_05/nicos_00000135.hdf",
        "0147": "v20/2019_04_05/nicos_00000136.hdf",
        "0148": "v20/2019_04_05/nicos_00000137.hdf",
        "0149": "v20/2019_04_05/nicos_00000138.hdf",
        "0150": "v20/2019_04_05/nicos_00000139.hdf",
        "0151": "v20/2019_04_05/nicos_00000140.hdf",
        "0152": "v20/2019_04_05/nicos_00000141.hdf",
        "0153": "v20/2019_04_05/nicos_00000142.hdf",
        "0154": "v20/2019_04_05/nicos_00000143.hdf",
        "0155": "v20/2019_04_05/nicos_00000144.hdf",
        "0156": "v20/2019_04_05/nicos_00000145.hdf",
        "0157": "v20/2019_04_05/nicos_00000146.hdf",
        "0158": "v20/2019_04_05/nicos_00000147.hdf",
        "0159": "v20/2019_04_05/nicos_00000148.hdf",
        "0160": "v20/2019_04_05/nicos_00000149.hdf",
        "0161": "v20/2019_04_05/nicos_00000150.hdf",
        "0162": "v20/2019_04_05/nicos_00000151.hdf",
        "0163": "v20/2019_04_05/nicos_00000152.hdf",
        "0164": "v20/2019_04_05/nicos_00000153.hdf",
        "0165": "v20/2019_04_05/nicos_00000154.hdf",
        "0166": "v20/2019_04_05/nicos_00000155.hdf",
        "0167": "v20/2019_04_05/nicos_00000156.hdf",
        "0168": "v20/2019_04_05/nicos_00000157.hdf",
        "0169": "v20/2019_04_05/nicos_00000158.hdf",
        "0170": "v20/2019_04_05/nicos_00000159.hdf",
        "0171": "v20/2019_04_05/nicos_00000160.hdf",
        "0172": "v20/2019_04_05/nicos_00000161.hdf",
        "0173": "v20/2019_04_05/nicos_00000162.hdf",
        "0174": "v20/2019_04_05/nicos_00000163.hdf",
        "0175": "v20/2019_04_05/nicos_00000164.hdf",
        "0176": "v20/2019_04_05/nicos_00000165.hdf",
        "0177": "v20/2019_04_05/nicos_00000166.hdf",
        "0178": "v20/2019_04_05/nicos_00000167.hdf",
        "0179": "v20/2019_04_05/nicos_00000168.hdf",
        "0180": "v20/2019_04_05/nicos_00000169.hdf",
        "0181": "v20/2019_04_05/nicos_00000170.hdf",
        "0182": "v20/2019_04_05/nicos_00000171.hdf",
        "0183": "v20/2019_04_05/nicos_00000172.hdf",
        "0184": "v20/2019_04_05/nicos_00000173.hdf",
        "0185": "v20/2019_04_05/nicos_00000174.hdf",
        "0186": "v20/2019_04_05/nicos_00000175.hdf",
        "0187": "v20/2019_04_05/nicos_00000176.hdf",
        "0188": "v20/2019_04_05/nicos_00000177.hdf",
        "0189": "v20/2019_04_05/nicos_00000178.hdf",
        "0190": "v20/2019_04_05/nicos_00000179.hdf",
        "0191": "v20/2019_04_05/nicos_00000180.hdf",
        "0192": "v20/2019_04_05/nicos_00000181.hdf",
        "0193": "v20/2019_04_05/nicos_00000182.hdf",
        "0194": "v20/2019_04_05/nicos_00000183.hdf",
        "0195": "v20/2019_04_05/nicos_00000184.hdf",
        "0196": "v20/2019_04_05/nicos_00000185.hdf",
        "0197": "v20/2019_04_05/nicos_00000186.hdf",
        "0198": "v20/2019_04_05/nicos_00000187.hdf",
        "0200": "v20/2019_04_05/v20-2019-03-05T21:31:14+0100.nxs",
        "0201": "v20/2019_04_05/v20-2019-03-06T02:08:01+0100.nxs",
        "0202": "v20/2019_04_05/v20-2019-03-06T11:18:37+0100.nxs",
        "0203": "v20/2019_04_05/v20-2019-03-06T11:42:41+0100.nxs",
        "0204": "v20/2019_04_05/v20-2019-03-06T15:19:24+0100.nxs",
        "0205": "v20/2019_04_05/v20-2019-03-06T16:21:11+0100.nxs",
        "0206": "v20/2019_04_05/v20-2019-03-06T18:07:30+0100.nxs",
        "0207": "v20/2019_04_05/v20-2019-03-08T12:55:36+0100.nxs",
        "0208": "v20/2019_04_05/v20-2019-03-08T14:45:20+0100.nxs",
        "0209": "v20/2019_04_05/v20-2019-03-08T15:48:53+0100.nxs",
        "0210": "v20/2019_04_05/v20-2019-03-08T18:07:53+0100.nxs",
        "0211": "v20/2019_04_05/v20-2019-03-08T19:04:37+0100.nxs",
        "0212": "v20/2019_04_05/v20-2019-03-08T20:28:05+0100.nxs",
        "0213": "v20/2019_04_05/v20-2019-03-08T21:32:56+0100.nxs",
        "0214": "v20/2019_04_05/v20-2019-03-08T22:33:53+0100.nxs",
        "0215": "v20/2019_04_05/v20-2019-03-09T00:30:20+0100.nxs",
        "0216": "v20/2019_04_05/v20-2019-03-09T01:30:02+0100.nxs",
        "0217": "v20/2019_04_05/v20-2019-03-09T02:10:30+0100.nxs",
        "0218": "v20/2019_04_05/v20-2019-03-09T03:02:51+0100.nxs",
        "0219": "v20/2019_04_05/v20-2019-03-09T03:41:22+0100.nxs",
        "0220": "v20/2019_04_05/v20-2019-03-09T09:17:25+0100.nxs",
        "0221": "v20/2019_04_05/v20-2019-03-09T11:33:40+0100.nxs",
        "0222": "v20/2019_04_05/v20-2019-03-09T12:10:38+0100.nxs",
        "0223": "v20/2019_04_05/v20-2019-03-09T17:18:49+0100.nxs",
        "0224": "v20/2019_04_05/v20-2019-03-09T17:27:05+0100.nxs",
        "0225": "v20/2019_04_05/v20-2019-03-09T19:27:48+0100.nxs",
        "0226": "v20/2019_04_05/v20-2019-03-09T20:14:16+0100.nxs",
        "0227": "v20/2019_04_05/v20-2019-03-09T21:59:45+0100.nxs",
        "0228": "v20/2019_04_05/v20-2019-03-09T23:54:11+0100.nxs",
        "0229": "v20/2019_04_05/v20-2019-03-10T06:11:51+0100.nxs",
        "0230": "v20/2019_04_05/v20-2019-03-10T11:05:00+0100.nxs",
        "0231": "v20/2019_04_05/v20-2019-03-10T11:14:59+0100.nxs",
        "0232": "v20/2019_04_05/v20-2019-03-10T11:29:28+0100.nxs",
        "0233": "v20/2019_04_05/v20-2019-03-10T11:37:24+0100.nxs",
        "0234": "v20/2019_04_05/v20-2019-03-10T12:00:23+0100.nxs",
        "0235": "v20/2019_04_05/v20-2019-03-10T12:22:45+0100.nxs",
        "0236": "v20/2019_04_05/v20-2019-03-10T13:17:23+0100.nxs",
        "0237": "v20/2019_04_05/v20-2019-03-10T15:13:00+0100.nxs",
        "0238": "v20/2019_04_05/v20-2019-03-10T17:16:58+0100.nxs",
        "0239": "v20/2019_04_05/v20-2019-03-10T18:35:35+0100.nxs",
        "0240": "v20/2019_04_05/v20-2019-03-10T19:12:31+0100.nxs",
        "0241": "v20/2019_04_05/v20-2019-03-11T08:25:10+0100.nxs",
        "0242": "v20/2019_04_05/v20-2019-04-04T17:16:20+0200.nxs",
        "0243": "v20/2019_04_05/v20-2019-04-04T17:17:03+0200.nxs",
        "0244": "v20/2019_04_05/v20-2019-04-08T16:01:12+0200.nxs",
        "0245": "v20/2019_04_05/v20-2019-04-08T16:02:40+0200.nxs"
    }

    inv_map = {v: k for k, v in sourceFolderArray.items()}

    def __init__(self):
        self.filename = "v20.h5"

    def get_h5_info(self, key):

        self.nexusInfo = {}


        filename = self.basename+self.sfdict[key] 
        if '.hdf' in filename:
            pass
        else:
            return

        f = h5py.File(filename, 'r',  libver='latest', swmr=True)

        self.nexusInfo["creator"] = self.get_attribute(f.attrs, "creator")
        self.nexusInfo["file_name"] = self.get_attribute(f.attrs, "file_name")
        self.nexusInfo["file_time"] = self.get_attribute(f.attrs, "file_time")
        title = self.get_property(f, "/entry/title")
        self.nexusInfo["title"] = title
        source_name = self.get_property(f, "/entry/instrument/source/name")
        self.nexusInfo["start_time"] = self.get_property(
            f, "/entry/start_time")
        sample_description = self.get_ellipsis(f, "/entry/sample/description")
        self.nexusInfo["sample_description"] = sample_description[()]
        self.nexusInfo["source_name"] = source_name
        f.close()
        print(self.nexusInfo)
        tag = filename.replace("/users/detector/experiments/", "")
        self.metadata[key] = self.nexusInfo

    def get_names(self, my_list, f, tag):
        if tag in f:
            names = f[tag+"/name"]
            my_list.extend(names)

    def get_attribute(self, attrs, attr):
        value = ""
        if (attr in attrs.keys()):
            value = attrs[attr]
        return value

    def get_property(self, f, path):
        title2 = ""
        if (path in f):
            title = f[path][...]
            title2 = title[()]
        # print(path, title2)
        return title2

    def get_ellipsis(self, f, path):
        if (path in f):
            dset = f[path]
        return dset[...]

    def loop(self):
        hostname = socket.gethostname()
        self.sfdict = self.sourceFolderArray
        if hostname == 'CI0020036':
            self.sfdict = {
                "0001": "nicos_00000108.hdf"
            }
            self.basename = "./"
        for key in self.sfdict:
            self.get_h5_info(key )


if __name__ == "__main__":
    h5 = GetNexusInfo()
    h5.loop()

    print(json.dumps(h5.metadata, indent=2, sort_keys=True))

    filename = "metadata.json"
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(h5.metadata, f, indent=2, sort_keys=True)
