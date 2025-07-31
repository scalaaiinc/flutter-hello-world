// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:flutter_hello_world/main.dart';

void main() {
  testWidgets('Hello World app smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());

    // Verify that our app displays the correct text.
    expect(find.text('Hello, World!'), findsOneWidget);
    expect(find.text('Welcome to Flutter on AWS Fargate'), findsOneWidget);
    expect(find.text('Flutter Hello World'), findsOneWidget); // AppBar title

    // Verify that the Flutter Dash icon is present.
    expect(find.byIcon(Icons.flutter_dash), findsOneWidget);
  });
}
