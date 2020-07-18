export const createContactForm =
  `mutation CreateContactForm($name: String!, $email: String!, $message: String!) {
    createContactForm(name: $name, email: $email, message: $message) {
      id
    }
  }`