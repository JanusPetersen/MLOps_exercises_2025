package main

import (
	"fmt"
	"Temp_exercise_module/mypackage"
	"os"
	"strconv"
)



func main(){
	var temperature float64
    var unit string
	var temp_temperature float64
	var final_temp int
	var tempStr string

	// fmt.Println("Write the temperature you want to convert in the format: 'Tempereture unit'")
	// fmt.Scanln(&temperature, &unit)

	tempStr = os.Args[1]
	unit = os.Args[2]

	temperature, _ = strconv.ParseFloat(tempStr, 64)

	switch unit {
		case "c":
			temp_temperature = mypackage.CelsiusToFahrenheit(temperature)
			final_temp = int(temp_temperature)
			fmt.Printf("%d Fahrenheit\n", final_temp)
		case "f":
			temp_temperature = mypackage.FahrenheitToCelsius(temperature)
			final_temp = int(temp_temperature)
			fmt.Printf("%d Celsius\n", final_temp)
		default:
			fmt.Println("The type have to be only C or F")
	}

}