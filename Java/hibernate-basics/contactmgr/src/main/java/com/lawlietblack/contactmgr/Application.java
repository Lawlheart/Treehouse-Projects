package com.lawlietblack.contactmgr;

import com.lawlietblack.contactmgr.model.Contact;
import com.lawlietblack.contactmgr.model.Contact.ContactBuilder;
import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.service.ServiceRegistry;

import java.util.List;

public class Application {
    // Hold a reusable reference to a session factory
    private static final SessionFactory sessionFactory = buildSessionFactory();

    private static SessionFactory buildSessionFactory() {
        // Create a StandardServiceRegistry
        final ServiceRegistry registry = new StandardServiceRegistryBuilder().configure().build();
        return new MetadataSources(registry).buildMetadata().buildSessionFactory();
    }

    public static void main(String[] args) {
        Contact contact = new ContactBuilder("Kenneth", "Black")
            .withEmail("kb@thevoid.com")
            .withPhone(5555555555L)
            .build();
        System.out.println(contact);
        int id = save(contact);

        //Before
        System.out.println("\n\nBEFORE\n\n");
        fetchAllContacts().stream().forEach(System.out::println);

        // Get the contact & update
        Contact c = findContactById(id);
        c.setFirstName("Lawliet");

        // persist
        delete(c);

        //After
        System.out.println("\n\nAFTER\n\n");
        fetchAllContacts().stream().forEach(System.out::println);
    }

    private static Contact findContactById(int id) {
        // Open a session
        Session session = sessionFactory.openSession();

        // Retrieve the Contact or null
        Contact contact = session.get(Contact.class, id);

        // Close the session
        session.close();

        //return the contact
        return contact;
    }

    private static void update(Contact contact) {
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        session.update(contact);
        session.getTransaction().commit();
        session.close();
    }

    private static void delete(Contact contact) {
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        session.delete(contact);

        session.getTransaction().commit();
        session.close();
    }

    @SuppressWarnings("unchecked")
    private static List<Contact> fetchAllContacts() {
        // Open a session
        Session session = sessionFactory.openSession();

        // Create Criteria
        Criteria criteria = session.createCriteria(Contact.class);

        // Get a list of Contact objects based on criteria
        List<Contact> contacts = criteria.list();

        // Close the session
        session.close();

        return contacts;
    }

    private static int save(Contact contact) {
        // Open a Session
        Session session = sessionFactory.openSession();

        // Begin a Transaction
        session.beginTransaction();

        // Use the session to save the contact
        int id = (int) session.save(contact);

        // Commit the transaction
        session.getTransaction().commit();

        // Close the session
        session.close();

        return id;
    }
}
