import React from 'react';
import LensSwitcher from './components/LensSwitcher';
import Editor from './components/Editor';
import RetentionSidebar from './components/RetentionSidebar';
import './index.css';

function App() {
  return (
    <div className="annie-app-container">
      <LensSwitcher />
      <Editor />
      <RetentionSidebar />
    </div>
  );
}

export default App;
