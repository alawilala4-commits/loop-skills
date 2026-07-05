# API Scaffold

Minimal FastAPI endpoint template for loop-backend skill.

## Usage

\`\`\`bash
cp -r scaffolds/api my-api-endpoint
cd my-api-endpoint
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
\`\`\`
