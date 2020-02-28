public class GrassHopper {

  public static char getGrade(final int s1, final int s2, final int s3) {
    final int score = (s1 + s2 + s3) / 3;

    if(score < 60) return 'F';
    if(score < 70) return 'D';
    if(score < 80) return 'C';
    if(score < 90) return 'B';
    return 'A';
  }

}
