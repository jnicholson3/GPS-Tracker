class gpgga:
    def __init__(self, messageid, utctime, lat, ns, long, ew, pfi, satused, hdop, msl_alt, msl_alt_units,
                 geiod_sep, geiod_sep_units, agediff_corr, diff_ref_stationid):
        self.messageid = messageid
        self.utctime = utctime
        self.lat = lat
        self.ns = ns
        self.long = long
        self.ew = ew
        self.pfi = pfi
        self.satused = satused
        self.hdop = hdop
        self.msl_alt = msl_alt
        self.msl_alt_units = msl_alt_units
        self.geiod_sep = geiod_sep
        self.geiod_sep_units = geiod_sep_units
        self.agediff_corr = agediff_corr
        self.diff_ref_stationid = diff_ref_stationid

    def nmea_gpgga_init(self, nmea_parsed):
        gpgga_struct = gpgga(nmea_parsed[0], nmea_parsed[1], nmea_parsed[2], nmea_parsed[3], nmea_parsed[4],
                             nmea_parsed[5],
                             nmea_parsed[6], nmea_parsed[7], nmea_parsed[8], nmea_parsed[9], nmea_parsed[10],
                             nmea_parsed[11],
                             nmea_parsed[12], nmea_parsed[13], nmea_parsed[14])
        return gpgga_struct

    def convertutc(self):
        formattedutc = self.utctime[0:2] + ":" + self.utctime[2:4] + ":"\
                       + self.utctime[4:6] + "." + self.utctime[7:10]
        return formattedutc

    def calculate_latitude(self):
        degree = self.lat[0:2]
        minutes = self.lat[2:9]
        latitude = float(degree) + (float(minutes)/60.0)
        if self.ns == 'S':
            latitude *= -1
        return latitude

    def calculate_longitude(self):
        degree = self.long[0:3]
        minutes = self.long[3:10]
        longitude = float(degree) + (float(minutes)/60.0)
        if self.ew == 'W':
            longitude *= -1
        return longitude

    def print_fields(self):
        print("MessageID: " + self.messageid)
        print("UTC Time: " + self.convertutc())
        print("Lat: " + str(self.calculate_latitude()))
        print("NS: " + self.ns)
        print("Long: " + str(self.calculate_longitude()))
        print("EW: " + self.ew)
        # print("Position Fix Indicator: " + self.pfi)
        # print("Satellites Used: " + self.satused)
        # print("HDOP: " + self.hdop)
        # print("MSL Altitude: " + self.msl_alt)
        # print("MSL Altitude Units: " + self.msl_alt_units)
        # print("Geiod Separation: " + self.geiod_sep)
        # print("Geiod Separation Units: " + self.geiod_sep_units)
        # print("Age of Diff. Corr: " + self_sentence.agediff_corr)
        # print("Diff. Ref. Station ID: " + self.diff_ref_stationid)
