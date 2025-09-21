from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://neondb_owner:npg_THfJAVd8Wg7R@ep-twilight-morning-agy4hf0i.c-2.eu-central-1.aws.neon.tech/math_frown_harm_460307"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("DELETE FROM blog_post"))
    print(f"Deleted {result.rowcount} rows from blog_post.")
