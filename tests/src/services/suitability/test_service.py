import pytest
from unittest.mock import patch
from .stubs import (
    stub_unique_id,
    stub_suitability_doc,
    StubPymongoResults,
    stub_suitability_answers,
    stub_suitability_empty_answers,
)
from func.src.domain.exceptions.exceptions import (
    ErrorOnUpdateUser,
    ErrorOnFindUser,
    NoSuitabilityAnswersFound,
    SuitabilityEmptyValues,
    InvalidOnboardingCurrentStep,
)
from func.src.services.suitability import SuitabilityService


@patch(
    "func.src.services.suitability.UserRepository.find_one_by_unique_id",
    return_value=False,
)
@pytest.mark.asyncio
async def test_when_user_not_exists_then_raises_error(mock_find_one):
    with pytest.raises(ErrorOnFindUser):
        await SuitabilityService._update_suitability_in_user_db(
            unique_id=stub_unique_id, suitability_doc=stub_suitability_doc
        )


@patch(
    "func.src.services.suitability.UserRepository.update_one_with_suitability_data",
    return_value=StubPymongoResults(),
)
@patch(
    "func.src.services.suitability.UserRepository.find_one_by_unique_id",
    return_value=True,
)
@pytest.mark.asyncio
async def test_when_update_suitability_user_fail_then_raises_error(
    mock_find_one, mock_update_one
):
    with pytest.raises(ErrorOnUpdateUser):
        await SuitabilityService._update_suitability_in_user_db(
            unique_id=stub_unique_id, suitability_doc=stub_suitability_doc
        )


@patch(
    "func.src.services.suitability.UserRepository.update_one_with_suitability_data",
    return_value=StubPymongoResults(True),
)
@patch(
    "func.src.services.suitability.UserRepository.find_one_by_unique_id",
    return_value=True,
)
@pytest.mark.asyncio
async def test_when_update_suitability_user_success_then_mock_was_called(
    mock_find_one, mock_update_one
):
    await SuitabilityService._update_suitability_in_user_db(
        unique_id=stub_unique_id, suitability_doc=stub_suitability_doc
    )
    mock_find_one.assert_called_once_with(unique_id=stub_unique_id)
    mock_update_one.assert_called_once_with(user=True, suitability=stub_suitability_doc)


@patch(
    "func.src.services.suitability.UserRepository.update_one_with_suitability_data",
    return_value=StubPymongoResults(True),
)
@patch(
    "func.src.services.suitability.UserRepository.find_one_by_unique_id",
    return_value=True,
)
@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_when_update_suitability_user_success_then_return_true(
    mock_find_one, mock_update_one
):
    result = await SuitabilityService._update_suitability_in_user_db(
        unique_id=stub_unique_id, suitability_doc=stub_suitability_doc
    )

    assert result is True


@patch(
    "func.src.services.suitability.SuitabilityRepository.find_one_most_recent_suitability_answers",
    return_value=stub_suitability_answers,
)
@pytest.mark.asyncio
async def test_when_get_suitability_success_then_return_answer_score_and_version(
    mock_find_most_recent_suitability,
):
    answers, score, version = await SuitabilityService._get_suitability_answers()

    assert isinstance(answers, list)
    assert isinstance(score, float)
    assert isinstance(version, int)


@patch(
    "func.src.services.suitability.SuitabilityRepository.find_one_most_recent_suitability_answers",
    return_value=False,
)
@pytest.mark.asyncio
async def test_when_get_suitability_return_none_then_raises(
    mock_find_most_recent_suitability,
):
    with pytest.raises(NoSuitabilityAnswersFound):
        await SuitabilityService._get_suitability_answers()


@patch(
    "func.src.services.suitability.SuitabilityRepository.find_one_most_recent_suitability_answers",
    return_value=stub_suitability_empty_answers,
)
@pytest.mark.asyncio
async def test_when_get_suitability_return_empty_values_then_raises(
    mock_find_most_recent_suitability,
):
    with pytest.raises(SuitabilityEmptyValues):
        await SuitabilityService._get_suitability_answers()


@patch(
    "func.src.services.suitability.SuitabilityService._update_suitability_in_user_db"
)
@patch("func.src.services.suitability.Audit.record_message_log")
@patch(
    "func.src.services.suitability.SuitabilityRepository.find_one_most_recent_suitability_answers",
    return_value=stub_suitability_answers,
)
@pytest.mark.asyncio
async def test_when_create_suitability_success_then_return_true(
    mock_answers, mock_audit, mock_insert_suitability
):
    result = await SuitabilityService.set_on_user(unique_id=stub_unique_id)

    assert result is True


@pytest.mark.asyncio
@patch(
    "func.src.services.suitability.OnboardingSteps.get_user_current_step",
    return_value="suitability",
)
async def test_when_current_step_correct_then_return_true(mock_onboarding_steps):
    result = await SuitabilityService.validate_current_onboarding_step(
        jwt="123"
    )

    assert result is True


@pytest.mark.asyncio
@patch(
    "func.src.services.suitability.OnboardingSteps.get_user_current_step",
    return_value="finished",
)
async def test_when_current_step_invalid_then_return_raises(mock_onboarding_steps):
    with pytest.raises(InvalidOnboardingCurrentStep):
        await SuitabilityService.validate_current_onboarding_step(jwt="123")
