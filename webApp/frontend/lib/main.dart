import 'package:flutter/material.dart';
import 'package:frontend/profile.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TrainingApp',
      home: const Profiles()
    );
  }
}