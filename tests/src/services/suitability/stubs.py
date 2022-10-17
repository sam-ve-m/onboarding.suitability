from func.src.domain.suitability.model import SuitabilityModel

stub_suitability_answers = {
    "_id": "Stub ObjectId 626a7955762933ead0922d7f",
    "score": 1.0,
    "suitability_version": 7,
    "suitability_submission_date": "date_stub",
    "answers": [
        {
            "question": "Quando você pretende utilizar os recursos investidos?",
            "question_id": 1,
            "question_score": 98,
            "answer": "Após 5 anos",
            "answer_weight": 384,
        },
        {
            "question": "Em caso de uma eventual necessidade, suas reservas financeiras equivalem a quantos meses de suas despesas?",
            "question_id": 2,
            "question_score": 99,
            "answer": "Mais de 12 meses",
            "answer_weight": 388,
        },
        {
            "question": "Quanto de seu patrimônio total (reservas financeiras, imóveis e outros bens) é destinado a investimentos financeiros?",
            "question_id": 3,
            "question_score": 100,
            "answer": "Mais de 60%",
            "answer_weight": 391,
        },
        {
            "question": "Qual é o seu objetivo de investimento?",
            "question_id": 4,
            "question_score": 101,
            "answer": "Obter rentabilidade elevada, aceitando o risco de expressivas oscilações do valor principal investido.",
            "answer_weight": 395,
        },
        {
            "question": "Suponha que em um mês, seus investimentos se desvalorizem significativamente, por exemplo de R$ 50 mil para R$ 30 mil, o que você faria?",
            "question_id": 5,
            "question_score": 102,
            "answer": "Aproveitaria para aplicar mais",
            "answer_weight": 398,
        },
        {
            "question": "Indique os produtos que mais representam seu conhecimento e experiência com investimentos nos últimos 3 anos:",
            "question_id": 6,
            "question_score": 103,
            "answer": "Investimentos indicados nas alternativas anteriores +  derivativos e/ou COE",
            "answer_weight": 402,
        },
        {
            "question": "Considerando sua experiência com investimentos, formação acadêmica e experiência profissional, como você define seu conhecimento sobre mercado o financeiro?",
            "question_id": 7,
            "question_score": 104,
            "answer": "Conheço os principais produtos, de renda fixa a ações, e já investi em alguns ou vários deles",
            "answer_weight": 405,
        },
    ],
}
stub_suitability_empty_answers = {
    "score": None,
    "suitability_version": 7,
    "suitability_submission_date": "date_stub",
    "answers": [
        {
            "question": "Quando você pretende utilizar os recursos investidos?",
            "question_id": 1,
            "question_score": 98,
            "answer": "Após 5 anos",
            "answer_weight": 384,
        },
        {
            "question": "Em caso de uma eventual necessidade, suas reservas financeiras equivalem a quantos meses de suas despesas?",
            "question_id": 2,
            "question_score": 99,
            "answer": "Mais de 12 meses",
            "answer_weight": 388,
        },
        {
            "question": "Quanto de seu patrimônio total (reservas financeiras, imóveis e outros bens) é destinado a investimentos financeiros?",
            "question_id": 3,
            "question_score": 100,
            "answer": "Mais de 60%",
            "answer_weight": 391,
        },
        {
            "question": "Qual é o seu objetivo de investimento?",
            "question_id": 4,
            "question_score": 101,
            "answer": "Obter rentabilidade elevada, aceitando o risco de expressivas oscilações do valor principal investido.",
            "answer_weight": 395,
        },
        {
            "question": "Suponha que em um mês, seus investimentos se desvalorizem significativamente, por exemplo de R$ 50 mil para R$ 30 mil, o que você faria?",
            "question_id": 5,
            "question_score": 102,
            "answer": "Aproveitaria para aplicar mais",
            "answer_weight": 398,
        },
        {
            "question": "Indique os produtos que mais representam seu conhecimento e experiência com investimentos nos últimos 3 anos:",
            "question_id": 6,
            "question_score": 103,
            "answer": "Investimentos indicados nas alternativas anteriores +  derivativos e/ou COE",
            "answer_weight": 402,
        },
        {
            "question": "Considerando sua experiência com investimentos, formação acadêmica e experiência profissional, como você define seu conhecimento sobre mercado o financeiro?",
            "question_id": 7,
            "question_score": 104,
            "answer": "Conheço os principais produtos, de renda fixa a ações, e já investi em alguns ou vários deles",
            "answer_weight": 405,
        },
    ],
}
stub_unique_id = "db43b7ff-54b2-483c-afab-f686c7eef782"
stub_suitability_doc = {
    "suitability": {"score": 1.0, "submission_date": "date", "suitability_version": 7}
}


class StubPymongoResults:
    def __init__(self, matched_count: bool = False):
        self.matched_count = matched_count


stub_answers = [
    {
        "question": "Quando você pretende utilizar os recursos investidos?",
        "question_id": 1,
        "question_score": 98,
        "answer": "Após 5 anos",
        "answer_weight": 384,
    },
    {
        "question": "Em caso de uma eventual necessidade, suas reservas financeiras equivalem a quantos meses de suas despesas?",
        "question_id": 2,
        "question_score": 99,
        "answer": "Mais de 12 meses",
        "answer_weight": 388,
    },
    {
        "question": "Quanto de seu patrimônio total (reservas financeiras, imóveis e outros bens) é destinado a investimentos financeiros?",
        "question_id": 3,
        "question_score": 100,
        "answer": "Mais de 60%",
        "answer_weight": 391,
    },
    {
        "question": "Qual é o seu objetivo de investimento?",
        "question_id": 4,
        "question_score": 101,
        "answer": "Obter rentabilidade elevada, aceitando o risco de expressivas oscilações do valor principal investido.",
        "answer_weight": 395,
    },
    {
        "question": "Suponha que em um mês, seus investimentos se desvalorizem significativamente, por exemplo de R$ 50 mil para R$ 30 mil, o que você faria?",
        "question_id": 5,
        "question_score": 102,
        "answer": "Aproveitaria para aplicar mais",
        "answer_weight": 398,
    },
    {
        "question": "Indique os produtos que mais representam seu conhecimento e experiência com investimentos nos últimos 3 anos:",
        "question_id": 6,
        "question_score": 103,
        "answer": "Investimentos indicados nas alternativas anteriores +  derivativos e/ou COE",
        "answer_weight": 402,
    },
    {
        "question": "Considerando sua experiência com investimentos, formação acadêmica e experiência profissional, como você define seu conhecimento sobre mercado o financeiro?",
        "question_id": 7,
        "question_score": 104,
        "answer": "Conheço os principais produtos, de renda fixa a ações, e já investi em alguns ou vários deles",
        "answer_weight": 405,
    },
]
stub_score = 1.0
stub_version = 7

stub_suitability_model = SuitabilityModel(
    unique_id=stub_unique_id,
    answers=stub_answers,
    version=stub_version,
    score=stub_score,
)
