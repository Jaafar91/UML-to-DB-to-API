package ${PACKAGE}.repository;

import ${PACKAGE}.entity.${SINGLE_ROUTE_NAME_CAPITALIZE}Entity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ${SINGLE_ROUTE_NAME_CAPITALIZE}Repository extends JpaRepository<${SINGLE_ROUTE_NAME_CAPITALIZE}Entity, Integer> {
}

