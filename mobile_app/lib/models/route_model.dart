class RouteResult {
  final String bestRoute;
  final double score;
  final List<String> explanation;

  RouteResult({
    required this.bestRoute,
    required this.score,
    required this.explanation,
  });

  factory RouteResult.fromJson(Map<String, dynamic> json) {
    return RouteResult(
      bestRoute: json['best_route'],
      score: json['score'].toDouble(),
      explanation: List<String>.from(json['explanation']),
    );
  }
}
