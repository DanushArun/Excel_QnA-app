# AI-Powered XLSX Q&A application

## 📋 Project Overview
This project is a **Streamlit-based application** that allows users to upload an Excel (`.xlsx`) file and ask questions about the data using **Google's Generative AI API (Gemini)**. The app extracts text from the uploaded file and uses the **Google Generative AI** to generate meaningful responses based on the user's questions.

Live Link: http://34.93.45.103:8501

---

## 🧰 Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **Google Generative AI API (Gemini)**
- **dotenv**

---

## 📂 Project Structure
```
├── app.py             # Main application code
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (API keys)
├── README.md          # Project documentation (this file)
```

---

## ⚙️ Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/DanushArun/Excel-QnA-webapp.git
cd Excel-QnA-webapp
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
```

### 3️⃣ **Activate the Virtual Environment**
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5️⃣ **Set Up the `.env` File**
Create a `.env` file in the root directory and add your **Gemini API key**:
```
GEMINI_API_KEY=your_google_api_key_here
```

---

## 🚀 Running the Application
```bash
streamlit run app.py
```
This will open the Streamlit app in your default web browser.

---

## 🛠 How It Works
1. **Upload an Excel File:**
   - Users can upload `.xlsx` files containing tabular data.
2. **Ask a Question:**
   - Enter a question related to the uploaded data.
3. **Get an Answer:**
   - The app uses the Google Generative AI API to provide an answer based on the data.

---

## 🧪 Example Usage
1. **Upload File:**
   - Example: `Production_Analysis.xlsx`
2. **Ask a Question:**
   - "What bottleneck issues are mentioned?"
3. **Generated Answer:**
   - "Bottleneck issues mentioned include supply chain delays and equipment downtime."

🧪 Positive Test Cases: <br />
1. **Upload File:** <br />
   - Example: `Sales_Report.xlsx` <br />
   **Ask a Question:** <br />
   - "What was the total revenue for Q4?" <br />
   **Generated Answer:** <br />
   - "The total revenue for Q4 was $1,200,000." <br />
   
2. **Upload File:** <br />
   - Example: `Employee_Performance.xlsx` <br />
   **Ask a Question:** <br />
   - "Which employee had the highest sales in October?" <br />
   **Generated Answer:** <br />
   - "John Doe had the highest sales in October with $50,000." <br />
3. **Upload File:** <br />
   - Example: `Inventory_Management.xlsx` <br />
   **Ask a Question:** <br />
   - 	“Which items are out of stock?” <br />
   **Generated Answer:** <br />
   - “Items out of stock are Item A, Item B, and Item D." <br />
4. **Upload File:** <br />
   - Example: `Marketing_Campaign.xlsx` <br />
   **Ask a Question:** <br />
   - 	“Which campaign had the highest ROI?” <br />
   **Generated Answer:** <br />
   - “The campaign with the highest ROI was Campaign Alpha with 200%.” <br />
5. **Upload File:** <br />
   - Example: `Production_Analysis.xlsx` <br />
   **Ask a Question:** <br />
   - 	“What were the downtime reasons?” <br />
   **Generated Answer:** <br />
   - “Downtime reasons include equipment maintenance and power outages.” <br />  <br />
  
🧪 Negative Test Cases:  <br /> 
1. **Upload File:** <br />
   - Example: `Empty_File.xlsx` <br />
   **Ask a Question:** <br />
   - 	“What were the downtime reasons?” <br />
   **Generated Answer:** <br />
   - “Downtime reasons include equipment maintenance and power outages.” <br />
---

## 🛠 Troubleshooting
### Common Errors and Fixes:
- **Error: GEMINI_API_KEY not found**
  - Ensure the `.env` file is correctly set up with your API key.
- **Error: 404 Requested entity was not found**
  - Ensure you're using the correct model (e.g., `models/chat-bison-001`).
- **Error: 'GenerateContentResponse' object has no attribute 'result'**
  - Update your code to use `response.responses[0].text`.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Developed by Danush Arun
