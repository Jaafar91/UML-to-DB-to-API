package com.uda.examplestemp.repository;

import com.uda.examplestemp.model.AnimalEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AnimalRepository extends JpaRepository<AnimalEntity, Long> {
}

