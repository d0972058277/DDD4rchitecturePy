import pytest
from core import AggregateRoot, IDomainEvent


class ExampleDomainEvent(IDomainEvent):
    pass


class ExampleAggregate(AggregateRoot[int]):
    def __init__(self, id: int) -> None:
        super().__init__(id)

    def Execute(self) -> None:
        domain_event = ExampleDomainEvent()
        super()._add_domain_event(domain_event)


def test_init_with_id():
    # Given
    entity_id = 1
    aggregate = ExampleAggregate(entity_id)

    # When

    # Then
    assert aggregate.id == entity_id


def test_domain_events_initially_empty():
    # Given
    aggregate = ExampleAggregate(1)

    # When

    # Then
    assert len(aggregate.domain_events) == 0


def test_add_domain_event():
    # Given
    aggregate = ExampleAggregate(1)

    # When
    aggregate.Execute()

    # Then
    assert len(aggregate.domain_events) == 1
    assert isinstance(aggregate.domain_events[0], ExampleDomainEvent)


def test_clear_domain_events():
    # Given
    aggregate = ExampleAggregate(1)
    aggregate.Execute()

    # When
    aggregate.clear_domain_events()

    # Then
    assert len(aggregate.domain_events) == 0


def test_cannot_instantiate_abstract_class():
    # Assert
    with pytest.raises(TypeError):
        AggregateRoot(1)
