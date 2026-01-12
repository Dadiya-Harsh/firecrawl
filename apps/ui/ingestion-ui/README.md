# Firecrawl UI Template

This template provides an easy way to spin up a UI for Firecrawl using React. It includes a pre-built component that interacts with the Firecrawl API, allowing you to quickly set up a web crawling and scraping interface.

## ⚠️ Important Security Notice

**This template now uses environment variables for API configuration. For production use, it is still strongly recommended to move API interactions to a server-side implementation to protect your API keys.**

## Prerequisites

- Node.js (v14 or later recommended)
- npm

## Getting Started

1. Install dependencies:

   ```bash
   npm install
   ```

2. Set up your environment variables:
   Copy the example environment file and configure your API settings:

   ```bash
   cp env.example .env
   ```

   Then edit `.env` with your actual values:

   ```env
   FIRECRAWL_API_URL=http://localhost:3002
   FIRECRAWL_API_KEY=your-api-key-here
   ```

3. Start the development server:

   ```
   npm run dev
   ```

4. Open your browser and navigate to the port specified in your terminal

## Environment Variables

The following environment variables are supported:

- `FIRECRAWL_API_URL`: Your Firecrawl API server URL (local or hosted)
- `FIRECRAWL_API_KEY`: Your Firecrawl API key

These variables are loaded from:
1. `.env` file in the project root
2. `.env` file in the parent directory (apps/ui/)
3. `.env` file in the root project directory
4. `.env` file in the apps/api/ directory

## Customization

The main Firecrawl components are located in:
- `src/components/ingestion.tsx` - V0 API implementation
- `src/components/ingestionV1.tsx` - V1 API implementation

You can modify these files to customize the UI or add additional features.

## Security Considerations

For production use, consider the following security measures:

1. Move API interactions to a server-side implementation to protect your Firecrawl API key.
2. Implement proper authentication and authorization for your application.
3. Set up CORS policies to restrict access to your API endpoints.

## Learn More

For more information about Firecrawl and its API, visit the [Firecrawl documentation](https://docs.firecrawl.dev/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

The Firecrawl Ingestion UI Template is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the SDK, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Please note that while this SDK is MIT licensed, it is part of a larger project which may be under different licensing terms. Always refer to the license information in the root directory of the main project for overall licensing details.
