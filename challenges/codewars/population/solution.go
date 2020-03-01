package kata

func NbYear(p0 int, percent float64, aug int, p int) int {
	var years int = 0
	var pop float64 = float64(p0)
	var a float64 = float64(aug)
	percent = percent / 100.0
	for pop < float64(p) {
		years += 1
		pop += pop*percent + a
	}
	return years
}
