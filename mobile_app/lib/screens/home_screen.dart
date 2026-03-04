import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import '../services/api_service.dart';
import '../models/route_model.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final sourceController = TextEditingController();
  final destController = TextEditingController();
  RouteResult? result;

  static const LatLng center = LatLng(28.6139, 77.2090);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("UrbanSense+")),
      body: Column(
        children: [
          SizedBox(
            height: 300,
            child: GoogleMap(
              initialCameraPosition:
                  CameraPosition(target: center, zoom: 12),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8),
            child: TextField(
              controller: sourceController,
              decoration: const InputDecoration(labelText: "Source"),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8),
            child: TextField(
              controller: destController,
              decoration: const InputDecoration(labelText: "Destination"),
            ),
          ),
          ElevatedButton(
            child: const Text("Find Best Route"),
            onPressed: () async {
              final res = await ApiService.getBestRoute(
                  sourceController.text, destController.text);
              setState(() => result = res);
            },
          ),
          if (result != null)
            Padding(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Best Route: ${result!.bestRoute}"),
                  Text("Score: ${result!.score}"),
                  const Text("Why this route:"),
                  ...result!.explanation.map((e) => Text("• $e"))
                ],
              ),
            )
        ],
      ),
    );
  }
}
