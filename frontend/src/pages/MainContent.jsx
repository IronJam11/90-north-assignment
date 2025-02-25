import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Homepage from './auth/Homepage';
import LoginPage from './auth/LoginPage';
import RegisterPage from './auth/Registerpage';
import ChatPage from './chat/ChatPage';

export default function MainContent() {
  return (
    <div className="min-h-[calc(100vh-4rem)] ml-64 mr-72 pt-16 px-6">
      <div className="py-6">
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/loginpage" element={<LoginPage />} />
          <Route path="/registerpage" element={<RegisterPage />} />
          <Route path="/chat/:username2" element={<ChatPage />} />
          <Route 
            path="*" 
            element={
             <Homepage/>
            } 
          />
        </Routes>
      </div>
    </div>
  );
}
