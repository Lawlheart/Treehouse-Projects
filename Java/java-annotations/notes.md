# Built-in Annotations

@Override
 - Sends a message to the compiler to check if the annotated method properly overrides the built-in methods
 - If not, get compile-time error
@Deprecated
 - Sends a warning to users that a feature will likely be removed in future updates
 - Some IDEs cross it out, too
@SuppressWarnings
 - Apply to methods, suppresses the kind of warning specified
 - Basically don't use it if there is literally any way to fix the warning

ClassPath (-cp or -classpath)
 - designates what directory to compile from, relative to package top level
`javac -cp src src/com/lawlietblack/override/Main.java`
 - needs to be designated on compile and run time
`java -cp src com.lawlietblack.override.Main`

Directory (-d)
- designates where to output your class files
`javac -d out -cp src src/com/lawlietblack/override/Main.java`
- use the directory we outputted to as the classpath now
`java -cp out com.lawlietblack.override.Main`


Custom Annotations
- Create a new one with the @interface keyword
`public @interface Doc { ... }`
- Set up new Annotation Retention and Target Annotations
`@Retention(RetentionPolicy.RUNTIME)`
`@Target({ElementType.TYPE, ElementType.METHOD})`
- add parameters like so:
`String desc() default "";`
`String[] hashtags() default {};`


Reflection
- Get a class object like so: 
`Class<?> clazz = MathUtils.class;`
- Get all the Methods of a class. Use second one to get Declared methods
`Method[] methods = clazz.getMethods();`
`Method[] methods = clazz.getDeclaredMethods();`
- Check if a class has an annotation. (Doc.class is @Doc class)
`clazz.isAnnotationPresent(Doc.class)`


Method Methods
- Get Name
`m.getName()`
- Get Parameter Count
`m.getParameterCount()`
- Get Return Type, use .getSimpleName() for simple name
`m.getReturnType().getSimpleName()`
- Get modifiers (public, static, etc). Returns int, so use Modifier.toString() to get name
`Modifier.toString(m.getModifiers())`
