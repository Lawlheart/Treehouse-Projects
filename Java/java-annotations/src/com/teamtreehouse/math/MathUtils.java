package com.teamtreehouse.math;

import com.teamtreehouse.docgen.Doc;

import java.awt.geom.Point2D;

@Doc(desc = "Utility class for commonly used math functions")
public class MathUtils {
    private static final Double EPSILON = 0.0001;

    @Doc(desc = "Calculate the area of a triangle.",
        params = {"Coordinate a", "Coordinate b", "Coordinate c"},
        returnVal = "Returns Area of the Triangle")
    public static Double triangleArea(Point2D.Double a, Point2D.Double b, Point2D.Double c) {
        return 0.0;
    }

    @Doc(desc = "Get the distance between two points",
        params = {"Point a", "Point b"},
        returnVal = "Distance between points")
    public static Double distance(Point2D.Double a, Point2D.Double b) {
        return 0.0;
    }

    @Doc(desc = "Get the quadratic roots of 3 numbers",
        params = {"Integer a", "Integer b", "Integer c"},
        returnVal = "Array of Root Values")
    public static Double[] quadraticRoots(int a, int b, int c) {
        return new Double[]{};
    }

    @Doc(desc = "Displays the value of Epsilon")
    public static void epsilon() {

    }

    private static boolean arePointsClose(Point2D.Double a, Point2D.Double b) {
        return false;
    }
}