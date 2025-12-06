# StockBot UI

React + TypeScript frontend for the StockBot News Research Tool.

## Features

- 🎨 Modern, premium dark-themed UI
- 📱 Fully responsive design
- ⚡ Fast and lightweight with Vite
- 🔄 Real-time loading states
- ✨ Smooth animations and transitions
- 🎯 TypeScript for type safety

## Prerequisites

- Node.js 20.x or higher
- npm or yarn

## Installation

1. Install dependencies:

```bash
npm install
```

## Development

Start the development server:

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

## Building for Production

Build the production bundle:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Project Structure

```
ui/
├── src/
│   ├── App.tsx          # Main application component
│   ├── App.css          # Application styles
│   ├── main.tsx         # Application entry point
│   ├── index.css        # Global styles
│   └── assets/          # Static assets
├── index.html           # HTML template
├── package.json         # Dependencies and scripts
├── tsconfig.json        # TypeScript configuration
└── vite.config.ts       # Vite configuration
```

## API Configuration

The frontend connects to the backend API at `http://localhost:8000` by default.

To change the API URL, update the `API_BASE_URL` constant in `src/App.tsx`:

```typescript
const API_BASE_URL = "http://localhost:8000";
```

## Usage

1. **Start the Backend API**: Make sure the FastAPI backend is running at `http://localhost:8000`

2. **Enter URLs**: Input up to 3 news article URLs in the sidebar

3. **Process URLs**: Click "Process URLs" to load and analyze the articles

4. **Ask Questions**: Once processing is complete, enter your question and click "Ask"

5. **View Results**: See the AI-generated answer with source citations

## Technologies Used

- **React 18**: UI library
- **TypeScript**: Type-safe JavaScript
- **Vite**: Fast build tool and dev server
- **Axios**: HTTP client for API calls
- **CSS3**: Modern styling with animations

## Design Features

- **Dark Theme**: Easy on the eyes with a modern color scheme
- **Gradient Buttons**: Eye-catching call-to-action buttons
- **Smooth Animations**: Fade-in and slide-in effects
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Loading States**: Clear feedback during API calls
- **Error Handling**: User-friendly error messages

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### Issue: API connection failed

**Solution**: Ensure the backend API is running at `http://localhost:8000`

### Issue: CORS errors

**Solution**: The backend has CORS middleware configured for `http://localhost:5173`. If using a different port, update the CORS settings in the backend.

### Issue: Build errors

**Solution**: Delete `node_modules` and `package-lock.json`, then run `npm install` again

## License

This project is part of the stock-bot-ai application.
