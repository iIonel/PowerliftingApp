import 'package:flutter/material.dart';
import 'package:frontend/profile.dart';

import 'location.dart';

class Exercises extends StatefulWidget {
  const Exercises({Key? key}) : super(key: key);

  @override
  State<Exercises> createState() => _ExercisesState();
}

class _ExercisesState extends State<Exercises> {
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
      body: Column(
        children: <Widget>[
          enum DropdownMenuEnt, label: label)
        ],
      )
    );
  }
}