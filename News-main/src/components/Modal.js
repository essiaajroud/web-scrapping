import React from 'react';
import './Modal.css';
import logo from '../logo.png'; // Assurez-vous d'avoir un fichier logo.png dans le dossier src

function Modal({ article, onClose }) {
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-button" onClick={onClose}>×</button>
        <img src={logo} alt="Logo" className="modal-logo" />
        <h2>{article.title}</h2>
        <p>{article.content}</p>
      </div>
    </div>
  );
}

export default Modal;
