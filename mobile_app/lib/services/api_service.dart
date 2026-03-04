import 'dart:convert';
import 'package:http/http.dart' as http;
import '../config/app_config.dart';
import '../models/route_model.dart';

class ApiService {
  static Future<RouteResult> getBestRoute(
      String source, String destination) async {

    final response = await http.post(
      Uri.parse('${AppConfig.backendUrl}/route'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        "source": source,
        "destination": destination,
        "travel_mode": "car"
      }),
    );

    return RouteResult.fromJson(jsonDecode(response.body));
  }
}
