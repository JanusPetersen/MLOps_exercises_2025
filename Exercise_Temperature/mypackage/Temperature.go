package mypackage

func CelsiusToFahrenheit(c float64) float64 {
	var result float64
	result = (c * 9.0 / 5.0) + 32
	return result
}

func FahrenheitToCelsius(f float64) float64 {
	var result float64
	result = (f - 32) * 5 / 9
	return result
}