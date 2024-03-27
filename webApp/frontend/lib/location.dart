import 'package:flutter/material.dart';
import 'package:frontend/exercise.dart';
import 'package:frontend/profile.dart';

class Locations extends StatefulWidget {
  const Locations({Key? key}) : super(key: key);

  @override
  State<Locations> createState() => _LocationsState();
}

class _LocationsState extends State<Locations> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        centerTitle: true,
        title: Row(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            IconButton(
              icon: const Icon(Icons.account_circle_sharp),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => Profiles()));
              },
            ),
            IconButton(
              icon: const Icon(Icons.fitness_center),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => Exercises()));
              },
            ),
            IconButton(
              icon: const Icon(Icons.place),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) => Locations()));
              },
            ),
          ],
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
          ],
        ),
      ),
    );
  }
}