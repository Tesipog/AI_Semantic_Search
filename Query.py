import pinecone
from sentence_transformers import SentenceTransformer

class QuestionSearch:
    def __init__(self):
        self.model = SentenceTransformer('all-mpnet-base-v2')
        pinecone.init(api_key='bc633d1d-54a8-4234-b24c-d5db4f5908a0', environment='asia-southeast1-gcp-free')
        self.index = pinecone.Index('question-search')

    def search(self, query, top_k=3):
        xq = self.model.encode([query]).tolist()
        result = self.index.query(xq, top_k=top_k, includeMetadata=True)
        Results_format = ""
        for match in result['matches']:
            Results_format += f"Id: {match['id']}\n"
            Results_format += f"Title: {match['metadata']['Title']}\n"
            Results_format += f"Answer: {match['metadata']['Answer']}\n"
            Results_format += f"Score: {match['score']}\n\n"
        return Results_format

# if __name__ == '__main__':
#     question_search = QuestionSearch()
#     query = "Africans freedom"
#     result = question_search.search(query)


