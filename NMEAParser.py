from gpgga import gpgga
import os.path
import pygmaps
import webbrowser


def sort_nmea(filename):
    gpgga_packet = []
    i = 0

    with open(filename) as f:
        sentences = f.read().splitlines()

    for sentence in sentences:
        sentence_messageid = sentences[i][0:6]
        if sentence_messageid == '$GPGGA':
            gpgga_packet.append(sentence)
        i += 1

    f.close()
    return gpgga_packet


def parse_sentence(nmea_sent):
    result = 0

    tmp = nmea_sentence.split('*')
    length = len(tmp) - 1

    checksum = nmea_sent.split('*')[length]
    checksum_sentence = nmea_sent.split('$')
    checksum_sentence = checksum_sentence[1].split('*')[0]

    for i in checksum_sentence:
        result = result ^ ord(i)

    result = format(result, '02X')
    if result == checksum:
        return checksum_sentence
    else:
        return 1


if __name__ == "__main__":
    #nmea_sentence = "$GPGGA,120557.916,3016.0320,N,09744.5860,W,2,06,1.7,108.5,M,47.6,M,1.5,0000*7A"
    #nmea_sentence = "$GPGGA,120557.916,5058.7456,N,00647.0515,E,2,06,1.7,108.5,M,47.6,M,1.5,0000*7A"
    #nmea_sentence = "$GPGGA,120558.916,5058.7457,N,00647.0514,E,2,06,1.7,109.0,M,47.6,M,1.5,0000*71"
    file = "samples4.txt"
    list_lat_long = []
    if os.path.exists(file):
        packet = sort_nmea(file)
        #print(packet)
        for nmea_sentence in packet:
            NMEA_Parsed = nmea_sentence.split(',')

            if nmea_sentence.startswith('$GPGGA'):
                nmea_parsed_gpgga = parse_sentence(nmea_sentence)
                if nmea_parsed_gpgga != 1:
                    nmea_parsed = nmea_parsed_gpgga.split(",")

                    gpgga_sentence = gpgga.nmea_gpgga_init(None, nmea_parsed)
                    list_lat_long.append((gpgga_sentence.calculate_latitude(), gpgga_sentence.calculate_longitude()))
                    #gpgga_sentence.print_fields()
                else:
                    print("Checksum didn't check out!")
    else:
        print("file doesn't exist.")

    #print(list_lat_long)
    mymap = pygmaps.maps(gpgga_sentence.calculate_latitude(), gpgga_sentence.calculate_longitude(), 12)
    mymap.addpoint(gpgga_sentence.calculate_latitude(), gpgga_sentence.calculate_longitude(), "#0000FF")
    mymap.addradpoint(gpgga_sentence.calculate_latitude(), gpgga_sentence.calculate_longitude(), 95, "#FF0000")
    mymap.addpath(list_lat_long, "#00FF00")
    mymap.draw('mymap.draw.html')
    url = 'mymap.draw.html'

    answer = input('Would you like to see your route? Type y or n \n')
    if answer == 'y':
        webbrowser.open_new_tab(url)
    else:
        print("Goodbye.")







