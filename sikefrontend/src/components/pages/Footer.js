import React from 'react';
import '../styles/footer.css'; // Import the CSS file for styling

const Footer = () => {
  return (
    <footer className="homepage-footer">
      <div className="footer-section company-info">
        <p>&copy; SikePay Company 2022</p>
        <p>Contact Headquarters:</p>
        <p>Nairobi, Ruiru</p>
        <p>PO Box 12345-00100</p>
        <p>Phone: +254 123 456 789</p>
        <p>Email: sikepay@gmail.com</p>
      </div>
      <div className="footer-section social-media">
        <p>Follow us on social media:</p>
        <ul>
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Twitter</a></li>
          <li><a href="#">Instagram</a></li>
        </ul>
      </div>
      <div className="footer-section quick-links">
        <p>Quick Links:</p>
        <ul>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Business</a></li>
          <li><a href="#">Banking</a></li>
          <li><a href="#">About Us</a></li>
        </ul>
      </div>
    </footer>
  );
}

export default Footer;
