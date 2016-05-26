package com.teamtreehouse.docgen;

import com.teamtreehouse.math.MathUtils;

import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

public class Main {
    public static void main(String[] args) {
        // TODO: Process the MathUtils class's annotations
        DocProcessor.process(MathUtils.class);
    }
}