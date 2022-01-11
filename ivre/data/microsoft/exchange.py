#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of IVRE.
# Copyright 2011 - 2021 Pierre LALET <pierre@droids-corp.org>
#
# IVRE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IVRE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IVRE. If not, see <http://www.gnu.org/licenses/>.


"""
This sub-module contains data to match Exchange build numbers to versions
"""

EXCHANGE_BUILDS = {
    # GENERATED_DATA_EXCHANGE_BUILD
    "4.0.837": "Exchange Server 4.0 Standard Edition",
    "4.0.838": "Exchange Server 4.0 SP1",
    "4.0.993": "Exchange Server 4.0 SP2",
    "4.0.994": "Exchange Server 4.0 SP3",
    "4.0.995": "Exchange Server 4.0 SP4",
    "4.0.996": "Exchange Server 4.0 SP5",
    "5.0.1457": "Exchange Server 5.0",
    "5.0.1458": "Exchange Server 5.0 SP1",
    "5.0.1460": "Exchange Server 5.0 SP2",
    "5.5.1960": "Exchange Server version 5.5",
    "5.5.2232": "Exchange Server version 5.5 SP1",
    "5.5.2448": "Exchange Server version 5.5 SP2",
    "5.5.2650": "Exchange Server version 5.5 SP3",
    "5.5.2653": "Exchange Server version 5.5 SP4",
    "6.0.4417": "Exchange 2000 Server",
    "6.0.4712": "Exchange 2000 Server SP1",
    "6.0.5762": "Exchange 2000 Server SP2",
    "6.0.6249": "Exchange 2000 Server SP3",
    "6.0.6487": "Exchange 2000 Server post-SP3",
    "6.0.6556": "Exchange 2000 Server post-SP3",
    "6.0.6603": "Exchange 2000 Server post-SP3",
    "6.0.6620.5": "Exchange 2000 Server post-SP3",
    "6.0.6620.7": "Exchange 2000 Server post-SP3",
    "6.5.6944": "Exchange Server 2003",
    "6.5.7226": "Exchange Server 2003 SP1",
    "6.5.7653.33": "Exchange Server 2003 post-SP2",
    "6.5.7654.4": "Exchange Server 2003 post-SP2",
    "6.5.7683": "Exchange Server 2003 SP2",
    "8.0.685.25": "Exchange Server 2007 RTM",
    "8.0.708.3": "Update Rollup 1 for Exchange Server 2007",
    "8.0.711.2": "Update Rollup 2 for Exchange Server 2007",
    "8.0.730.1": "Update Rollup 3 for Exchange Server 2007",
    "8.0.744.0": "Update Rollup 4 for Exchange Server 2007",
    "8.0.754.0": "Update Rollup 5 for Exchange Server 2007",
    "8.0.783.2": "Update Rollup 6 for Exchange Server 2007",
    "8.0.813.0": "Update Rollup 7 for Exchange Server 2007",
    "8.1.240.6": "Exchange Server 2007 SP1",
    "8.1.263.1": "Update Rollup 1 for Exchange Server 2007 SP1",
    "8.1.278.2": "Update Rollup 2 for Exchange Server 2007 SP1",
    "8.1.291.2": "Update Rollup 3 for Exchange Server 2007 SP1",
    "8.1.311.3": "Update Rollup 4 for Exchange Server 2007 SP1",
    "8.1.336.1": "Update Rollup 5 for Exchange Server 2007 SP1",
    "8.1.340.1": "Update Rollup 6 for Exchange Server 2007 SP1",
    "8.1.359.2": "Update Rollup 7 for Exchange Server 2007 SP1",
    "8.1.375.2": "Update Rollup 8 for Exchange Server 2007 SP1",
    "8.1.393.1": "Update Rollup 9 for Exchange Server 2007 SP1",
    "8.1.436.0": "Update Rollup 10 for Exchange Server 2007 SP1",
    "8.2.176.2": "Exchange Server 2007 SP2",
    "8.2.217.3": "Update Rollup 1 for Exchange Server 2007 SP2",
    "8.2.234.1": "Update Rollup 2 for Exchange Server 2007 SP2",
    "8.2.247.2": "Update Rollup 3 for Exchange Server 2007 SP2",
    "8.2.254.0": "Update Rollup 4 for Exchange Server 2007 SP2",
    "8.2.305.3": "Update Rollup 5 for Exchange Server 2007 SP2",
    "8.3.83.6": "Exchange Server 2007 SP3",
    "8.3.106.2": "Update Rollup 1 for Exchange Server 2007 SP3",
    "8.3.137.3": "Update Rollup 2 for Exchange Server 2007 SP3",
    "8.3.159.2": "Update Rollup 3-v2 for Exchange Server 2007 SP3",
    "8.3.192.1": "Update Rollup 4 for Exchange Server 2007 SP3",
    "8.3.213.1": "Update Rollup 5 for Exchange Server 2007 SP3",
    "8.3.245.2": "Update Rollup 6 for Exchange Server 2007 SP3",
    "8.3.264.0": "Update Rollup 7 for Exchange Server 2007 SP3",
    "8.3.279.3": "Update Rollup 8 for Exchange Server 2007 SP3",
    "8.3.279.5": "Update Rollup 8-v2 for Exchange Server 2007 SP3",
    "8.3.279.6": "Update Rollup 8-v3 for Exchange Server 2007 SP3",
    "8.3.297.2": "Update Rollup 9 for Exchange Server 2007 SP3",
    "8.3.298.3": "Update Rollup 10 for Exchange Server 2007 SP3",
    "8.3.327.1": "Update Rollup 11 for Exchange Server 2007 SP3",
    "8.3.342.4": "Update Rollup 12 for Exchange Server 2007 SP3",
    "8.3.348.2": "Update Rollup 13 for Exchange Server 2007 SP3",
    "8.3.379.2": "Update Rollup 14 for Exchange Server 2007 SP3",
    "8.3.389.2": "Update Rollup 15 for Exchange Server 2007 SP3",
    "8.3.406.0": "Update Rollup 16 for Exchange Server 2007 SP3",
    "8.3.417.1": "Update Rollup 17 forExchange Server 2007 SP3",
    "8.3.445.0": "Update Rollup 18 forExchange Server 2007 SP3",
    "8.3.459.0": "Update Rollup 19 forExchange Server 2007 SP3",
    "8.3.468.0": "Update Rollup 20 for Exchange Server 2007 SP3",
    "8.3.485.1": "Update Rollup 21 for Exchange Server 2007 SP3",
    "8.3.502.0": "Update Rollup 22 for Exchange Server 2007 SP3",
    "8.3.517.0": "Update Rollup 23 for Exchange Server 2007 SP3",
    "14.0.639.21": "Exchange Server 2010 RTM",
    "14.0.682.1": "Update Rollup 1 for Exchange Server 2010",
    "14.0.689.0": "Update Rollup 2 for Exchange Server 2010",
    "14.0.694.0": "Update Rollup 3 for Exchange Server 2010",
    "14.0.702.1": "Update Rollup 4 for Exchange Server 2010",
    "14.0.726.0": "Update Rollup 5 for Exchange Server 2010",
    "14.1.218.15": "Exchange Server 2010 SP1",
    "14.1.255.2": "Update Rollup 1 for Exchange Server 2010 SP1",
    "14.1.270.1": "Update Rollup 2 for Exchange Server 2010 SP1",
    "14.1.289.7": "Update Rollup 3 for Exchange Server 2010 SP1",
    "14.1.323.6": "Update Rollup 4 for Exchange Server 2010 SP1",
    "14.1.339.1": "Update Rollup 5 for Exchange Server 2010 SP1",
    "14.1.355.2": "Update Rollup 6 for Exchange Server 2010 SP1",
    "14.1.421.0": "Update Rollup 7 for Exchange Server 2010 SP1",
    "14.1.421.2": "Update Rollup 7 v2 for Exchange Server 2010 SP1",
    "14.1.421.3": "Update Rollup 7 v3 for Exchange Server 2010 SP1",
    "14.1.438.0": "Update Rollup 8 for Exchange Server 2010 SP1",
    "14.2.247.5": "Exchange Server 2010 SP2",
    "14.2.283.3": "Update Rollup 1 for Exchange Server 2010 SP2",
    "14.2.298.4": "Update Rollup 2 for Exchange Server 2010 SP2",
    "14.2.309.2": "Update Rollup 3 for Exchange Server 2010 SP2",
    "14.2.318.2": "Update Rollup 4 for Exchange Server 2010 SP2",
    "14.2.318.4": "Update Rollup 4 v2 for Exchange Server 2010 SP2",
    "14.2.328.10": "Update Rollup 5 v2 for Exchange Server 2010 SP2",
    "14.2.342.3": "Update Rollup 6 Exchange Server 2010 SP2",
    "14.2.375.0": "Update Rollup 7 for Exchange Server 2010 SP2",
    "14.2.390.3": "Update Rollup 8 for Exchange Server 2010 SP2",
    "14.3.123.4": "Exchange Server 2010 SP3",
    "14.3.146.0": "Update Rollup 1 for Exchange Server 2010 SP3",
    "14.3.158.1": "Update Rollup 2 for Exchange Server 2010 SP3",
    "14.3.169.1": "Update Rollup 3 for Exchange Server 2010 SP3",
    "14.3.174.1": "Update Rollup 4 for Exchange Server 2010 SP3",
    "14.3.181.6": "Update Rollup 5 for Exchange Server 2010 SP3",
    "14.3.195.1": "Update Rollup 6 for Exchange Server 2010 SP3",
    "14.3.210.2": "Update Rollup 7 for Exchange Server 2010 SP3",
    "14.3.224.2": "Update Rollup 8 v2 for Exchange Server 2010 SP3",
    "14.3.235.1": "Update Rollup 9 for Exchange Server 2010 SP3",
    "14.3.248.2": "Update Rollup 10 for Exchange Server 2010 SP3",
    "14.3.266.2": "Update Rollup 11 for Exchange Server 2010 SP3",
    "14.3.279.2": "Update Rollup 12 for Exchange Server 2010 SP3",
    "14.3.294.0": "Update Rollup 13 for Exchange Server 2010 SP3",
    "14.3.301.0": "Update Rollup 14 for Exchange Server 2010 SP3",
    "14.3.319.2": "Update Rollup 15 for Exchange Server 2010 SP3",
    "14.3.328.5": "Update Rollup 5 for Exchange Server 2010 SP2",
    "14.3.336.0": "Update Rollup 16 for Exchange Server 2010 SP3",
    "14.3.352.0": "Update Rollup 17 for Exchange Server 2010 SP3",
    "14.3.361.1": "Update Rollup 18 for Exchange Server 2010 SP3",
    "14.3.382.0": "Update Rollup 19 for Exchange Server 2010 SP3",
    "14.3.389.1": "Update Rollup 20 for Exchange Server 2010 SP3",
    "14.3.399.2": "Update Rollup 21 for Exchange Server 2010 SP3",
    "14.3.411.0": "Update Rollup 22 for Exchange Server 2010 SP3",
    "14.3.417.1": "Update Rollup 23 for Exchange Server 2010 SP3",
    "14.3.419.0": "Update Rollup 24 for Exchange Server 2010 SP3",
    "14.3.435.0": "Update Rollup 25 for Exchange Server 2010 SP3",
    "14.3.442.0": "Update Rollup 26 for Exchange Server 2010 SP3",
    "14.3.452.0": "Update Rollup 27 for Exchange Server 2010 SP3",
    "14.3.461.1": "Update Rollup 28 for Exchange Server 2010 SP3",
    "14.3.468.0": "Update Rollup 29 for Exchange Server 2010 SP3",
    "14.3.496.0": "Update Rollup 30 for Exchange Server 2010 SP3",
    "14.3.509.0": "Update Rollup 31 for Exchange Server 2010 SP3",
    "14.3.513.0": "Update Rollup 32 for Exchange Server 2010 SP3",
    "15.0.516": "Exchange Server 2013 RTM",
    "15.0.620": "Exchange Server 2013 CU1",
    "15.0.712": "Exchange Server 2013 CU2",
    "15.0.775": "Exchange Server 2013 CU3",
    "15.0.847": "Exchange Server 2013 SP1",
    "15.0.913": "Exchange Server 2013 CU5",
    "15.0.995": "Exchange Server 2013 CU6",
    "15.0.1044": "Exchange Server 2013 CU7",
    "15.0.1076": "Exchange Server 2013 CU8",
    "15.0.1104": "Exchange Server 2013 CU9",
    "15.0.1130": "Exchange Server 2013 CU10",
    "15.0.1156": "Exchange Server 2013 CU11",
    "15.0.1178": "Exchange Server 2013 CU12",
    "15.0.1210": "Exchange Server 2013 CU13",
    "15.0.1236": "Exchange Server 2013 CU14",
    "15.0.1263": "Exchange Server 2013 CU15",
    "15.0.1293": "Exchange Server 2013 CU16",
    "15.0.1320": "Exchange Server 2013 CU17",
    "15.0.1347": "Exchange Server 2013 CU18",
    "15.0.1365": "Exchange Server 2013 CU19",
    "15.0.1367": "Exchange Server 2013 CU20",
    "15.0.1395": "Exchange Server 2013 CU21",
    "15.0.1473": "Exchange Server 2013 CU22",
    "15.0.1497": "Exchange Server 2013 CU23",
    "15.1.225": "Exchange Server 2016 Preview / Exchange Server 2016 RTM",
    "15.1.396": "Exchange Server 2016 CU1",
    "15.1.466": "Exchange Server 2016 CU2",
    "15.1.544": "Exchange Server 2016 CU3",
    "15.1.669": "Exchange Server 2016 CU4",
    "15.1.845": "Exchange Server 2016 CU5",
    "15.1.1034": "Exchange Server 2016 CU6",
    "15.1.1261": "Exchange Server 2016 CU7",
    "15.1.1415": "Exchange Server 2016 CU8",
    "15.1.1466": "Exchange Server 2016 CU9",
    "15.1.1531": "Exchange Server 2016 CU10",
    "15.1.1591": "Exchange Server 2016 CU11",
    "15.1.1713": "Exchange Server 2016 CU12",
    "15.1.1779": "Exchange Server 2016 CU13",
    "15.1.1847": "Exchange Server 2016 CU14",
    "15.1.1913": "Exchange Server 2016 CU15",
    "15.1.1979": "Exchange Server 2016 CU16",
    "15.1.2044": "Exchange Server 2016 CU17",
    "15.1.2106": "Exchange Server 2016 CU18",
    "15.1.2176": "Exchange Server 2016 CU19",
    "15.1.2242": "Exchange Server 2016 CU20",
    "15.1.2308": "Exchange Server 2016 CU21",
    "15.1.2375": "Exchange Server 2016 CU22",
    "15.2.196": "Exchange Server 2019 Preview",
    "15.2.221": "Exchange Server 2019 RTM",
    "15.2.330": "Exchange Server 2019 CU1",
    "15.2.397": "Exchange Server 2019 CU2",
    "15.2.464": "Exchange Server 2019 CU3",
    "15.2.529": "Exchange Server 2019 CU4",
    "15.2.595": "Exchange Server 2019 CU5",
    "15.2.659": "Exchange Server 2019 CU6",
    "15.2.721": "Exchange Server 2019 CU7",
    "15.2.792": "Exchange Server 2019 CU8",
    "15.2.858": "Exchange Server 2019 CU9",
    "15.2.922": "Exchange Server 2019 CU10",
    "15.2.986": "Exchange Server 2019 CU11",
    # GENERATED_DATA_EXCHANGE_BUILD
}