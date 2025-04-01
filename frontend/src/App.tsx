import React from 'react';
import { Beer } from 'lucide-react';

function App() {
  React.useEffect(() => {
    // Load Dialogflow messenger script
    const script = document.createElement('script');
    script.src = 'https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1';
    script.async = true;
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-100 to-amber-200">
      {/* Header */}
      <header className="bg-amber-800 text-white p-6 shadow-lg">
        <div className="container mx-auto flex items-center gap-3">
          <Beer size={32} />
          <h1 className="text-3xl font-bold">BrewCompass</h1>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-2xl mx-auto">
          <div className="bg-white rounded-lg shadow-xl p-6 mb-8">
            <h2 className="text-2xl font-semibold text-amber-800 mb-4">Your Conversational Beer Guide</h2>
            <p className="text-gray-600 mb-4">
              Welcome to BrewCompass, your personal beer recommendation assistant! Whether you're a craft beer enthusiast or just starting your beer journey, I'm here to help you discover your next favorite brew.
            </p>
            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <h3 className="text-lg font-medium text-amber-800 mb-2">Try asking me:</h3>
              <ul className="space-y-2 text-amber-700">
                <li>• "What's a good beer for beginners?"</li>
                <li>• "Recommend a craft IPA"</li>
                <li>• "What beer pairs well with pizza?"</li>
                <li>• "Tell me about stout beers"</li>
              </ul>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-semibold text-amber-800 mb-3">Expert Recommendations</h3>
              <p className="text-gray-600">
                Get personalized beer suggestions based on your taste preferences and experience level.
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-semibold text-amber-800 mb-3">Food Pairings</h3>
              <p className="text-gray-600">
                Discover the perfect beer to complement your favorite dishes.
              </p>
            </div>
          </div>
        </div>
      </main>

      {/* Dialogflow Messenger */}
      <df-messenger
        intent="WELCOME"
        chat-title="BrewCompass"
        agent-id="1c557561-a95d-4c12-b305-5427589d86d6"
        language-code="en"
      ></df-messenger>

      {/* Custom styles for df-messenger */}
      <style>
        {`
          df-messenger {
            z-index: 999;
            position: fixed;
            bottom: 16px;
            right: 16px;
          }
          
          df-messenger {
            --df-messenger-bot-message: #815723;
            --df-messenger-button-titlebar-color: #92400e;
            --df-messenger-chat-background-color: #fef3c7;
            --df-messenger-font-color: white;
            --df-messenger-user-message: #92400e;
          }
        `}
      </style>
    </div>
  );
}

export default App;