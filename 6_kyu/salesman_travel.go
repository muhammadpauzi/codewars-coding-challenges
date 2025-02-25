package main

import (
	"fmt"
	"strings"
)

const ad = `
123 Main Street St. Louisville OH 43071, 432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,
54 Holy Grail Street Niagara Town ZP 32908, 3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,
10 Pussy Cat Rd. Chicago EX 34342, 10 Gordon St. Atlanta RE 13000, 58 Gordon Road Atlanta RE 13000,
22 Tokyo Av. Tedmondville SW 43098, 674 Paris bd. Abbeville AA 45521, 10 Surta Alley Goodtown GG 30654,
45 Holy Grail Al. Niagara Town ZP 32908, 320 Main Al. Bern AE 56210, 14 Gordon Park Atlanta RE 13000,
100 Pussy Cat Rd. Chicago EX 34342, 2 Gordon St. Atlanta RE 13000, 5 Gordon Road Atlanta RE 13000,
2200 Tokyo Av. Tedmondville SW 43098, 67 Paris St. Abbeville AA 45521, 11 Surta Avenue Goodtown GG 30654,
45 Holy Grail Al. Niagara Town ZP 32918, 320 Main Al. Bern AE 56215, 14 Gordon Park Atlanta RE 13200,
100 Pussy Cat Rd. Chicago EX 34345, 2 Gordon St. Atlanta RE 13222, 5 Gordon Road Atlanta RE 13001,
2200 Tokyo Av. Tedmondville SW 43198, 67 Paris St. Abbeville AA 45522, 11 Surta Avenue Goodville GG 30655,
2222 Tokyo Av. Tedmondville SW 43198, 670 Paris St. Abbeville AA 45522, 114 Surta Avenue Goodville GG 30655,
2 Holy Grail Street Niagara Town ZP 32908, 3 Main Rd. Bern AE 56210, 77 Gordon St. Atlanta RE 13000,
100 Pussy Cat Rd. Chicago OH 13201`

func Travel(r, zipcode string) string {
	addresses := strings.Split(r, ",")

	numbers := []string{}
	streets := []string{}

	for _, address := range addresses {
		splitedAddress := strings.Split(strings.TrimSpace(address), " ")

		// get only the street name without number on prefix and zip code on suffix
		street := strings.Join(splitedAddress[1:len(splitedAddress)-2], " ")
		// get the zip code on the last string address
		zipCodeOnTheAddress := strings.Join(splitedAddress[len(splitedAddress)-2:], " ")

		if zipCodeOnTheAddress == zipcode {
			numbers = append(numbers, splitedAddress[0])

			streets = append(streets, street)
		}
	}
	return fmt.Sprintf("%s:%s/%s", zipcode, strings.Join(streets, ","), strings.Join(numbers, ","))
}

func main() {

	fmt.Println(Travel(ad, "AA 45522"))
	fmt.Println("AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670")
	fmt.Println(Travel(ad, "OH 430"), "OH 430:/")
}

// package kata

// import "strings"

// func Travel(r, zipcode string) string {
// 	var strInfo []string
// 	var strNumbers []string

// 	for _, str := range strings.Split(r, ",") {
// 		tmp := strings.Fields(str)
// 		if zipcode == strings.Join(tmp[(len(tmp) - 2):], " ") {
// 			strNumbers = append(strNumbers, tmp[0])
// 			strInfo = append(strInfo, strings.Join(tmp[1:len(tmp) - 2], " "))
// 		}
// 	}

// 	return zipcode + ":" + strings.Join(strInfo, ",") + "/" + strings.Join(strNumbers, ",")
// }
