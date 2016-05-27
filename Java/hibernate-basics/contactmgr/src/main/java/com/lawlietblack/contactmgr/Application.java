package com.lawlietblack.contactmgr;

import com.lawlietblack.contactmgr.model.Contact;
import com.lawlietblack.contactmgr.model.Contact.ContactBuilder;
import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.service.ServiceRegistry;

public class Application {
    // Hold a reusable reference to a session factory
//    private static final SessionFactory sessionFactory = buildSessionFactory();

//    private static SessionFactory buildSessionFactory() {
//        // Create a StandardServiceRegistry
//        final ServiceRegistry registry = new StandardServiceRegistryBuilder().configure().build();
//        return new MetadataSources(registry).buildMetadata().buildSessionFactory();
//    }

    public static void main(String[] args) {
        Contact contact = new ContactBuilder("Kenneth", "Black")
            .withEmail("kb@thevoid.com")
            .withPhone(5555555555L)
            .build();
        System.out.println(contact);
    }
}
