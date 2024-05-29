def enrich_data(session, source, destination):
    error_message = {"lambda": "lambda-commercial-mx-segmentation-enrich"}
    #TODO fazer filtro MX
    query_get_data = f"SELECT * FROM {source};"
    logger.info(f"Running Query: {query_get_data}")
    logger.info(f"Copying data from {source} to {destination}")
    result = session.execute(query_get_data)
    
    #Copy Data from source to destination with person code from BRM
    query_copy_data = f'''INSERT INTO {destination} (
                            business_model
                            , company
                            , country
                            , created_at
                            , created_by
                            , person_id
                            , person_code
                            , row_uid
                            , status
                            , subsegmentation_id
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    query_prepared = session.prepare(query_copy_data)
    
    for row in result:
        try:
            person = get_person(row.person_id)
            person_id = person.get('personId', uuid.UUID(int=0))
            session.execute(query_prepared, (row.business_model, row.company, row.country, row.created_at, row.created_by, 
                                             person_id, row.person_code, row.row_uid, row.status, row.subsegmentation_id))
            logger.info(f"{row}\nData inserted successfully\nperson_id: {person_id} + person_id: {row.person_code}")
        except Exception as e:
            logger.error({'status': 'FAILURE', 'error': str(e)})
        
    logger.info(f"Finished enrich_data")
    return True