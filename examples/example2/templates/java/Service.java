package ${PACKAGE}.service;

import ${PACKAGE}.mapper.*;
import ${PACKAGE}.model.*;
import ${PACKAGE}.entity.${SINGLE_ROUTE_NAME_CAPITALIZE}Entity;
import ${PACKAGE}.repository.${SINGLE_ROUTE_NAME_CAPITALIZE}Repository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class ${SINGLE_ROUTE_NAME_CAPITALIZE}Service {

    private final ${SINGLE_ROUTE_NAME_CAPITALIZE}Repository ${SINGLE_ROUTE_NAME}Repository;
    private final ${SINGLE_ROUTE_NAME_CAPITALIZE}Mapper ${SINGLE_ROUTE_NAME}Mapper;
    private final GenericResponseMapper genericResponseMapper;

    public GenericResponse getAll() {
        return genericResponseMapper.map(
            null,
            ${SINGLE_ROUTE_NAME_CAPITALIZE}Data.builder().${SINGLE_ROUTE_NAME}(
                ${SINGLE_ROUTE_NAME}Repository.findAll().stream().map(x -> ${SINGLE_ROUTE_NAME}Mapper.map(x)).collect(Collectors.toList())
            ).build());
    }

    public GenericResponse getOne(${ROUTE_UNIQUE_DATATYPE} ${ROUTE_UNIQUE}) {
        return genericResponseMapper.map(
            null,
            ${SINGLE_ROUTE_NAME}Mapper.map(
                ${SINGLE_ROUTE_NAME}Repository.findBy${ROUTE_UNIQUE_CAPITALIZE}(${ROUTE_UNIQUE}).get()
            ));
    }
    

    public GenericResponse createOne(${SINGLE_ROUTE_NAME_CAPITALIZE} ${SINGLE_ROUTE_NAME}) {
        ${SINGLE_ROUTE_NAME}Repository.save(${SINGLE_ROUTE_NAME}Mapper.map(${SINGLE_ROUTE_NAME}));
        return genericResponseMapper.map(
            null,
            null
            );
    }

    public GenericResponse deleteOne(${ROUTE_UNIQUE_DATATYPE} ${ROUTE_UNIQUE}) {
        
        ${SINGLE_ROUTE_NAME}Repository.delete(${SINGLE_ROUTE_NAME}Repository.findBy${ROUTE_UNIQUE_CAPITALIZE}(${ROUTE_UNIQUE}).get());
        return genericResponseMapper.map(
            null,
            null);
    }
}
